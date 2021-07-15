def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = [0] * (N+1)
    Cnt_A = [0] * (N+1)
    for a in A:
        Cnt_A[a] += 1
        cnt = Cnt_A[a]
        C[cnt] += 1
    cum_C = []
    cu = 0
    for c in C:
        cu += c
        cum_C.append(cu)
    Ans = []
    for k in range(1, N+1):
        # K = k のとき、 n 組以上作れる <=> 使えるカードが nk 枚以上
        # n 組以上作れる <=> 同じカードは n 枚以下
        # 同じカードは n 枚以下で全体として nk 枚以上用意できるか？
        ok, ng = 0, N//k+1
        while ok + 1 < ng:
            n = ok+ng>>1
            if cum_C[n] >= n*k:
                ok = n
            else:
                ng = n
        Ans.append(ok)
    print(("\n".join(map(str, Ans))))

main()


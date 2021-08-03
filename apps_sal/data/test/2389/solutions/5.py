import sys
readline = sys.stdin.readline


def main():
    N, a, b, c = map(int, readline().split())
    A = {"A": a, "B": b, "C": c}
    S = []
    for i in range(N):
        l = readline().strip()
        S.append([l[0], l[1]])

    ans = ""
    ret = False
    for i in range(N):
        if A[S[i][0]] == 0 and A[S[i][1]] == 0:
            break
        if i == N - 1:
            if A[S[i][0]] > 0:
                ans += S[i][1]
            else:
                ans += S[i][0]
            ret = True
            break
        if A["A"] + A["B"] + A["C"] == 1:
            if A[S[i][0]] == 1:
                if S[i][0] in S[i + 1] and S[i][1] not in S[i + 1]:
                    break
                else:
                    A[S[i][0]] -= 1
                    A[S[i][1]] += 1
                    ans += S[i][1]
                    continue
            else:
                if S[i][1] in S[i + 1] and S[i][0] not in S[i + 1]:
                    break
                else:
                    A[S[i][0]] += 1
                    A[S[i][1]] -= 1
                    ans += S[i][0]
                    continue
        if A[S[i][0]] == 0:
            A[S[i][0]] += 1
            A[S[i][1]] -= 1
            ans += S[i][0]
            continue
        elif A[S[i][1]] == 0:
            A[S[i][0]] -= 1
            A[S[i][1]] += 1
            ans += S[i][1]
            continue
        elif S[i][0] in S[i + 1]:
            A[S[i][0]] += 1
            A[S[i][1]] -= 1
            ans += S[i][0]
            continue
        else:
            A[S[i][0]] -= 1
            A[S[i][1]] += 1
            ans += S[i][1]
            continue

    if ret:
        print("Yes")
        for i in range(N):
            print(ans[i])
    else:
        print("No")


def __starting_point():
    main()


__starting_point()

# ABC141E - Who Says a Pun?
def resolve():
    N = int(input())
    S = input().rstrip()
    ok, ng = 0, N // 2 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        flg = False
        memo = set()
        for i in range(N - 2 * mid + 1):
            memo.add(hash(S[i : i + mid]))
            if hash(S[i + mid : i + 2 * mid]) in memo:
                flg = True
                break
        if flg:
            ok = mid  # next mid will be longer
        else:
            ng = mid  # next mid will be shorter
    print(ok)  # max length of substrings appeared twice or more


resolve()


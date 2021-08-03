def solve(S):
    N = len(S)
    i = 0
    while i < N:
        if N - i < 5:
            return False
        if S[i: i + 5] == "dream":
            if i + 7 <= N and S[i + 5: i + 7] == "er":
                if i + 7 == N or S[i + 7] != "a":
                    i += 7
                else:
                    i += 5
            else:
                i += 5
        elif S[i: i + 5] == "erase":
            if i + 5 < N and S[i + 5] == "r":
                i += 6
            else:
                i += 5
        else:
            return False
    return True


S = input()
print("YES" if solve(S) else "NO")

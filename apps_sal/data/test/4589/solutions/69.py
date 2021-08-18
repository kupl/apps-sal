h, w = list(map(int, input().split()))
ans = [[0 for _ in range(w + 2)] for _ in range(h + 2)]

for i in range(h):
    S = input()
    for j, s in enumerate(S):
        if s == "
          ans[i + 1][j + 1] = "
           if ans[i][j + 1] != "
              ans[i][j + 1] += 1
            if ans[i + 1][j] != "
              ans[i + 1][j] += 1
            if ans[i][j] != "
              ans[i][j] += 1
            if ans[i + 1][j + 2] != "
              ans[i + 1][j + 2] += 1
            if ans[i][j + 2] != "
              ans[i][j + 2] += 1
            if ans[i + 2][j + 1] != "
              ans[i + 2][j + 1] += 1
            if ans[i + 2][j + 2] != "
              ans[i + 2][j + 2] += 1
            if ans[i + 2][j] != "
              ans[i + 2][j] += 1

for a in ans[1:-1]:
    print(("".join(map(str, a))[1:-1]))

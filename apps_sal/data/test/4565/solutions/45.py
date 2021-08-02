N = int(input())
S = list(input())

lst = [0] * N
Re = S.count("E")
Lw = 0

for i in range(N):
    if S[i] == "E":
        Re -= 1
        lst[i] = Re + Lw
    else:
        Lw += 1
        lst[i] = Re + Lw - 1

ans = min(lst)
print(ans)

S_ = list(input())
T = input()
#後ろから探索する

n = len(S_)
m = len(T)
nonexist = 1
for i in range(n-1, m-2, -1):
    flg = True
    for j in range(m):
        if (S_[i-j] != T[-j-1]) and (S_[i-j] != "?"):
            flg = False
            break
    if flg:
        nonexist = 0
        index = i
        break

if nonexist:
    print("UNRESTORABLE")
    return

index -= m-1
for i in range(m):
    S_[index+i] = T[i]

for i in range(n):
    if S_[i] == "?":
        S_[i] = "a"
print(("".join(S_)))


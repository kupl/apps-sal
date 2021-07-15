S = list(input())
T = list(input())
count = 0

for i in range(len(S)):
    if S[i] == T[i]:
        count += 1

if count == len(S) and len(T) == len(S) + 1:
    print("Yes")
else:
    print("No")

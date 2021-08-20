S = input()
T = input()
count = 0
m = len(T)
l = len(S) - len(T)
for i in range(0, l + 1):
    for j in range(0, len(T)):
        if S[j + i] != T[j]:
            count += 1
    if m > count:
        m = count
    count = 0
print(m)

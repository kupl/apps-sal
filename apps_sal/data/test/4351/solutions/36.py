n = input()
cnt = 0
for i in range(len(n)):
    if n[i] == n[-1-i]:
        cnt += 1
if cnt == len(n):
    print("Yes")
else:
    print("No")

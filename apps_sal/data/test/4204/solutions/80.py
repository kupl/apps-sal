s = input()
k = int(input())
cnt = 0
for i in s:
    if int(i) == 1:cnt += 1
    if cnt == k or int(i) != 1:
        print(i)
        break

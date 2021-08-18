import datetime


n, k = list(map(int, input().split()))
dislike = list(map(int, input().split()))
while True:
    for i in str(n):
        if int(i) not in dislike:
            continue
        else:
            break
    else:
        break
    n += 1
print(n)

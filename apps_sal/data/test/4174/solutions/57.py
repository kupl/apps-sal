N, X = list(map(int, input().split()))
Li = list(map(int, input().split()))

Di = 0
count = 1
for i in Li:
    Di = Di + i
    if Di <= X:
        count += 1
    else:
        break
print(count)

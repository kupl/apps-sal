n, k = map(int, input().split())
x = list(map(int, input().split()))

count = 0
count_list = []

for _ in x:
    count += 1
    if _ == 1:
        break

for _ in range(k):
    count_list.append((count-1-_-0.1)//(k-1)+(n-count+_-0.1)//(k-1)+2)

print(int(min(count_list)))

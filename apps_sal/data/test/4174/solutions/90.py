(A, B) = list(map(int, input().split(' ')))
l = list(map(int, input().split(' ')))
ans = 0
count = 1
for i in l:
    ans += i
    if ans <= B:
        count += 1
print(count)

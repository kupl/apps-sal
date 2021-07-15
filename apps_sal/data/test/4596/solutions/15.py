n = int(input())
a_list = list(map(int, input().split()))
new_list = []
ans = 0
while True:
    for i in a_list:
        if i % 2 == 1:
            break
        else:
            a = i // 2
            new_list.append(a)
    if len(new_list) < n:
        break
    ans += 1
    a_list = new_list
    new_list = []

print(ans)

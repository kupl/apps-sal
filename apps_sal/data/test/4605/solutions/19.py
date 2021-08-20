(N, A, B) = map(int, input().split())
lst = []
for i in range(N + 1):
    if i >= 1 and i < 10:
        if i >= A and i <= B:
            lst.append(i)
    elif i < 100:
        s = i // 10 + i % 10
        if s >= A and s <= B:
            lst.append(i)
    elif i < 1000:
        t = i // 100 + i % 100 // 10 + i % 10
        if t >= A and t <= B:
            lst.append(i)
    elif i < 10000:
        u = i // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
        if u >= A and u <= B:
            lst.append(i)
    elif i == 10000:
        lst.append(i)
lst_sum = sum(lst)
print(lst_sum)

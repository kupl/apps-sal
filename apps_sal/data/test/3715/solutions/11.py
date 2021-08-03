n = int(input())
days = input().split()
last = '0'
counter = 0
for i in range(n):
    if last == days[i] or days[i] == '0':
        counter += 1
        last = '0'
    else:
        if days[i] != '3':
            last = days[i]
        else:
            if last == '1':
                last = '2'
            elif last == '2':
                last = '1'
            else:
                if i < n - 1:
                    if days[i + 1] == '1':
                        last = '2'
                    elif days[i + 1] == '2':
                        last = '1'
print(counter)

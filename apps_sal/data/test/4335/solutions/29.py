n = int(input())
s = input()

if n % 2 == 1:
    print('No')
else:
    head = s[:n // 2]
    tail = s[n // 2:]

    if head == tail:
        print('Yes')
    else:
        print('No')

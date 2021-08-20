n = int(input())
if n % 2:
    end = 'I hate it'
else:
    end = 'I love it'
arr = []
for i in range(n - 1):
    if i % 2 == 0:
        arr.append('I hate that')
    else:
        arr.append('I love that')
arr.append(end)
print(' '.join(arr))

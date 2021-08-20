(n, k) = list(map(int, input().split()))
possible_names = [a + b for a in 'QWERTYUIOPLKJHGFDSAZXCVBNM' for b in 'qwertyuioplkjhgfdsazxcvbnm']
names = [possible_names.pop() for i in range(k - 1)]
for word in input().split():
    if word == 'YES':
        names.append(possible_names.pop())
    else:
        names.append(names[-k + 1])
print(*names)

n_input = int(input())
l_input = list(map(int, str(input()).split()))
l_binary = []
for _ in range(n_input):
    pop = l_input.pop() % 2
    if l_binary == []:
        l_binary.append(pop)
    elif pop == l_binary[-1]:
        l_binary.pop()
    else:
        l_binary.append(pop)
n = len(l_binary)
if n <= 1:
    print('YES')
else:
    print('NO')

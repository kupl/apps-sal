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


def solve(n, l_binary):
    if n <= 1:
        return 1
    elif n == 2:
        sum_l = sum(l_binary) % 2  # if sum_l = 0 return YES else return NO
        return sum_l - 1
    else:
        for k in range(n - 2):
            l_sequence = [l_binary[k], l_binary[k + 1], l_binary[k + 2]]
            if l_sequence == [0, 1, 0] or l_sequence == [1, 0, 1]:
                return 0
        return 1


if solve(len(l_binary), l_binary):
    print("YES")
else:
    print("NO")

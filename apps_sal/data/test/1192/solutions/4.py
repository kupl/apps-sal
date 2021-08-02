n, k = [int(x) for x in input().split()]
base = [int(x) for x in input().split()]


def invert_count(l):
    swaps = 0
    for i in range(len(l)):
        while i > 0 and l[i - 1] > l[i]:
            temp = l[i - 1]
            l[i - 1] = l[i]
            l[i] = temp
            swaps += 1
            i -= 1
    return swaps


def make_reflects(base, rem=k):
    if rem == 0:
        return invert_count(base)
    else:
        ans = 0
        for i in range(len(base)):
            for j in range(i + 1, len(base)):
                new = base[:i] + list(reversed(base[i:j + 1])) + base[j + 1:]
                ans += make_reflects(new, rem - 1)
        ans += n * make_reflects(base, rem - 1)
        return ans


total = make_reflects(base)
reflect_number = n * (n + 1) / 2
total_number = reflect_number ** k
ans = total / total_number

print('{0:.10f}'.format(ans))

input()
crush = [0] + [int(x) for x in input().split()]
visited = set()

circle_sizes = []

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    for i in range(len(crush)):
        if i not in visited:
            start, cur, count = i, i, 0
            while cur not in visited:
                visited.add(cur)
                count += 1
                cur = crush[cur]
            if cur != start:
                return -1
            circle_sizes.append(count if count % 2 else count // 2)
    
    if len(circle_sizes) == 1:
        return circle_sizes[0]
    
    ans = lcm(circle_sizes[0], circle_sizes[1])
    for size in circle_sizes[2:]:
        ans = lcm(ans, size)
    return ans

print(solve())


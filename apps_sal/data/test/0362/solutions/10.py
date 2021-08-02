# stdin=open('input.txt')

# def input():
# 	return stdin.readline()[:-1]

# a, b = map(int, input().split())

# l = list(map(int, input().split()))


# CODE BEGINS HERE.................

ans = 0
for t in range(2, int(input())):
    ans += t * (t + 1)

print(ans)
# CODE ENDS HERE....................

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, k = map(int, input().split())
p = [(x, i) for i, x in enumerate(list(map(int, input().split())), 1)]
p.sort(reverse = True)
print(p[k - 1][0])
print(' '.join(str(x[1]) for x in p[:k]))

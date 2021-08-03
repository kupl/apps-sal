import sys
def input(): return sys.stdin.readline().strip("\r\n")


n = int(input())
ans = []
for x, y in sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: abs(x[0]) + abs(x[1])):
    if x > 0:
        ans.append('1 %d R' % x)
    if x < 0:
        ans.append('1 %d L' % -x)
    if y > 0:
        ans.append('1 %d U' % y)
    if y < 0:
        ans.append('1 %d D' % -y)
    ans.append('2')
    if x > 0:
        ans.append('1 %d L' % x)
    if x < 0:
        ans.append('1 %d R' % -x)
    if y > 0:
        ans.append('1 %d D' % y)
    if y < 0:
        ans.append('1 %d U' % -y)
    ans.append('3')
print(len(ans))
print('\n'.join(ans))

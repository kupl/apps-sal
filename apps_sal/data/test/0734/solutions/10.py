import sys
input_file = sys.stdin

[n,m] = list(int(x) for x in input_file.readline().split())
stacks = list(int(x) for x in input_file.readline().split())
stacks.sort()

ans = 0
cur_stack = 0
cur_h = 0

while cur_stack < n:
    ans += 1
    if stacks[cur_stack] >= cur_h + 1:
        cur_h += 1
    cur_stack += 1
ans += stacks[-1] - cur_h 
    
print(sum(stacks) - ans)


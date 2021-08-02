from collections import deque

a, b, c = list(map(int, input().split()))
m = int(input())

usb_cost = []
ps_cost = []


for i in range(m):
    cost, t = input().split()
    cost = int(cost)

    if t == 'USB':
        usb_cost.append(cost)
    else:
        ps_cost.append(cost)


usb_cost.sort(reverse=True)
ps_cost.sort(reverse=True)

# print(usb_cost)
# print(ps_cost)

ans = 0
ans_sum = 0

for i in range(min(a, len(usb_cost))):
    ans_sum += usb_cost.pop()
    ans += 1

for i in range(min(b, len(ps_cost))):
    ans_sum += ps_cost.pop()
    ans += 1

all_types = sorted(usb_cost + ps_cost, reverse=True)

for i in range(min(c, len(all_types))):
    ans_sum += all_types.pop()
    ans += 1


print(ans, ans_sum)

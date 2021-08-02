n, m = map(int, input().split())
ac_cnt = set()
wa_cnt = 0
penalty = [0] * n
for i in range(m):
    p, s = input().split()
    num = int(p) - 1
    if num not in ac_cnt:
        if s == "AC":
            ac_cnt.add(num)
            wa_cnt += penalty[num]
        else:
            penalty[num] += 1
print(len(set(ac_cnt)), wa_cnt)

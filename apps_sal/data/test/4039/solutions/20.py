n, r = list(map(int, (input().split())))

proj_list = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    proj_list.append([b, a, True])

def check(proj_list):
    nonlocal r

    while len(proj_list) > 0:
        i = 0
        while True:
            if i == len(proj_list):
                for prj in proj_list:
                    if prj[2]:
                        return False
                return True

            proj = proj_list[i]
            if r >= proj[1] and proj[2]:
                proj[2] = False
                r += proj[0]
                if r < 0:
                    return False
                break
            i += 1


#proj_list.sort(reverse=True)
raise_mmr = [x for x in proj_list if x[0] >= 0]
hard_work = [x for x in proj_list if x[0] < 0]
proj_list = sorted(raise_mmr, key=lambda x: x[0], reverse=True) + sorted(hard_work, key=lambda x: x[1] + x[0], reverse=True)

print("YES" if check(proj_list) else "NO")


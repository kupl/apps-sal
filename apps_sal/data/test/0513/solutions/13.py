l = [[int(c) for c in input().split()] for i in range(8)]
xs = sorted(set([p[0] for p in l]))
ys = sorted(set([p[1] for p in l]))
if len(xs) != 3 or len(ys) != 3:
    print("ugly")
else:
    done = False
    for x in range(3):
        for y in range(3):
            if x == y == 1: continue
            if [xs[x],ys[y]] not in l:
                print("ugly")
                done = True
                break
        if done: break
    if not done:
        print("respectable")

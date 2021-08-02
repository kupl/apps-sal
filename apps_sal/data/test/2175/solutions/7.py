n = int(input());
water = (n + 2) * [0];
vol = [int(i) for i in input().split()];
trace = (n + 2) * [0];
next = [i + 1 for i in range(n + 2)];
m = int(input());
out = []
for i in range(m):
    c = [int(i) for i in input().split()];
    if c[0] == 1:
        w = c[2];
        k = c[1] - 1;
        r = 0;
        while((w > 0) and (k < n)):
            if(w <= vol[k] - water[k]):
                water[k] = water[k] + w;
                break;
            else:
                w = w - (vol[k] - water[k]);
                water[k] = vol[k];
                trace[r] = k;
                r = r + 1;
                k = next[k];
        for j in range(r):
            next[trace[j]] = k;
    if c[0] == 2:
        out.append(water[c[1] - 1]);
for i in out:
    print(i)

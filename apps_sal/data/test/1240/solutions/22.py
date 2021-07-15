n = int(input());
l = [0] * n;
r = [0] * n;

cur_res = 0;
for i in range(n):
    l[i], r[i] = [int(x) for x in input().split()];
    cur_res += l[i] - r[i];

max_res = abs(cur_res);
max_indx = -1;

for i in range(n):
    tmp_res = abs(cur_res - 2 * (l[i] - r[i]));
    if tmp_res > max_res:
        max_res = tmp_res;
        max_indx = i;

print((max_indx + 1));


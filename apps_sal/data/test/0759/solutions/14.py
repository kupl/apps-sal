h, m = map(int, input().split());
g, u, s, k = map(int, input().split());
d20 = ((g + k - 1) // k) * s;
v = (20 - h - 1) * 60 + (60 - m);
if v < 0:
    v = 0;
s2 = s - s / 5;
p20 = ((g + v * u + k - 1) // k) * s2;
print(min(d20, p20));

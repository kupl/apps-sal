n, m = map(int, input().split());
mas = [0] * (n + 1);
for i in range(m):
    a, b, c = map(int, input().split());
    mas[b] += c;
    mas[a] -= c;

sum = 0;
for i in mas:
    sum += max(i, -i);
print(int(sum / 2));

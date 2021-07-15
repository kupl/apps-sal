n = int(input());
cnt = 0;
for q in range(1, n // 2 + 1):
    if n % q == 0:
        cnt = cnt + 1;
print(cnt);

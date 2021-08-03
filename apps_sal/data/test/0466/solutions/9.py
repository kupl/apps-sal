problems = input().split()
c = int(problems[0])
d = int(problems[1])
n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
k = int(input())

t = n * m - k  # нужное воличество людей, кроме уже прошедших
ans = 100000000  # количество задач
i = 0
while i * n <= t:  # если число проходящих по основным раундам не больше, чем надо
    ans = min(ans, (t - i * n) * d + i * c)
    i += 1
ans = min(ans, i * c)
print(ans)

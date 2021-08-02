n = int(input())
ans1 = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) // 5040;
ans2 = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) // 720;
ans3 = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // 120;
print(ans1 + ans2 + ans3)

N = input()
List = [N[i] for i in range(len(N))]
ans = 0
for i in range(len(List)):
    ans += int(List[i])
    ans %= 9
if ans % 9 == 0:
    print("Yes")
else:
    print("No")

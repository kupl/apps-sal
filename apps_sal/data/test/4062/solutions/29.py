a,b,c,d = map(int, input().split())

Ans1 = a*c
Ans2 = a*d
Ans3 = b*c
Ans4 = b*d

nums = [Ans1, Ans2, Ans3, Ans4]
print(max(nums))

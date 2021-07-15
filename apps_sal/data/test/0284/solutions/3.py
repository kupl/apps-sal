n = int(input())
for a in range(2000):
    for b in range((n-1234567*a)//123456+50):
        rem = n - 1234567*a - 123456 * b
        if (rem%1234 == 0 and rem//1234 >= 0):
            print("YES")
            quit()
print("NO")


a = list(input())
a.sort()
# sortメソッドを使って、順番に並べる。
# たとえbcaでもcbaでもabcの順にしてくれる
if a[0] == 'a' and a[1] == 'b' and a[2] == 'c':
    print("Yes")
else:
    print("No")

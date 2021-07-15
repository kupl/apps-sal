#ABC062 B:PictureFrame

H,W = map(int, input().split())
pic = []
for _ in range(H):
    a = input()
    pic.append(a)
print('#'*(W+2))
for i in range(H):
    print('#' + pic[i] + '#')
print('#'*(W+2))

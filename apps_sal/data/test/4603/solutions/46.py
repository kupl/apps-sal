a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 電車の運賃リスト
train = [a,b]
# バスの運賃リスト
bus = [c,d]
# 電車のバスのそれぞれ最安値を足し合わせる
print(min(train)+ min(bus))

n = int(input())
a = list(input().split())
# aの中に黄色Yが含まれていればFourと出力
if "Y" in a:
    print("Four")
# aの中に黄色Yが含まれてなけれはThreeと出力
else:
    print("Three")

N = int(input())
color = list(input().split())

# 1つの袋があり、ひなあられが N個 入っています。
# 桃色を P、白色を W、緑色を G、黄色を Y と表したとき、袋からひなあられを1粒ずつ取り出していったところ、i番目に取り出したひなあられの色は Si でした。
# この袋に 3種類 のひなあられが入っていた場合は Three、4種類 のひなあられが入っていた場合は Four と出力してください。

if "Y" in color:
    print("Four")
else:
    print("Three")

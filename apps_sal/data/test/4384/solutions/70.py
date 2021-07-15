# N回目のコンテストの名前の最初の３文字を出力

N = int ( input ( ) )

if 1 <= N <= 999:
    print("ABC")
elif 1000 <= N <= 1998:
    print("ABD")
else:
    print("入力ミス")

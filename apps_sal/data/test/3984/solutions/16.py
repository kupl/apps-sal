a=list(input())
arr='z'
for item in a:
    if arr<item:
        print('Ann')
    else:
        print('Mike')
    if item<arr:
        arr=item


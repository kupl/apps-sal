import sys

def main():
    yes = True
    array = sys.stdin.readline().strip().split(' ')
    array1 = sys.stdin.readline().strip().split(' ')
    array2 = sys.stdin.readline().strip().split(' ')
    for i in range(len(array1)):
        if i < int(array[1])-1 or i >= int(array[2]):
            if array1[i] != array2[i]:
                yes = False
                break
    if yes:
        print("TRUTH")
    else:
        print("LIE")
    return


main()

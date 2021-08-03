def main():
    import sys
    material = input()
    scheme = input()
    flag = True
    for i in range(len(scheme)):
        if flag:
            if not scheme[i] in material:
                print(-1)
                flag = False
    if flag:
        counter = 0
        SIZE = len(scheme) - 1
        saver = []
        result = 0
        while counter <= SIZE:
            saver += [scheme[counter]]
            if (scheme.count(scheme[counter])
                    <= material.count(scheme[counter])):
                result += scheme.count(scheme[counter])
            else:
                result += material.count(scheme[counter])
            while scheme[counter] in saver:
                if counter < SIZE:
                    counter += 1
                else:
                    print(result)
                    return
        print(result)


main()

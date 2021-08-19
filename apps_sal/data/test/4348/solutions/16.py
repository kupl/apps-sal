(n, k) = list(map(int, input().split()))
s = input()
i = ord('a')
while 1:
    km = s.count(chr(i))
    if k - km > 0:
        k -= km
        i += 1
    else:
        break
ss = ''
for j in range(n):
    if ord(s[j]) > i:
        ss += s[j]
    elif ord(s[j]) == i:
        if k > 0:
            k -= 1
        else:
            ss += s[j]
print(ss)
'\n////////////////      //////        ///////      //             ///////     //  //   //\n////          //    ///   ///     ///    ///     //            ///  ///     ////     //\n////    ////       ///     ///   ///      ///    //           /////////     ////     ///////\n////     /////    ///       /// ///        ///   //          ///    ///     ////     //   //\n//////////////     ///////////   ///////////     //////     ///     ///     //  //   //   //\n'

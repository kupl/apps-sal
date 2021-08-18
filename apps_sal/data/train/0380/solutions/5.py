class Solution(object):

    def ipv4(self, ip):

        l = ip.split('.')
        if (len(l) != 4):
            return False
        for i in l:
            if (len(i) > 1 and i[0] == '0'):
                return False
            elif (i.isdigit() and (0 <= int(i) <= 255)):
                pass
            else:
                return False

        return True

    def ipv6(self, ip):
        l = ip.split(':')
        if (len(l) != 8):
            return False
        for i in l:
            if (len(i) > 4 or len(i) == 0):
                return False

            validset = set("123456789abcdefABCDEF0")

            for j in i:
                if j in validset:
                    pass
                else:
                    return False

        return True

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if(self.ipv4(IP)):
            return "IPv4"

        if(self.ipv6(IP)):
            return "IPv6"

        return "Neither"
